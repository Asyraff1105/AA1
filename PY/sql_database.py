import sqlite3

class DatabaseManager:
    def __init__(self, db_name='databaseexample.db'):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Initialize database with tables"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    content TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
    
    def create_user(self, name, email, age):
        """Create a new user"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
                    (name, email, age)
                )
                conn.commit()
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Error: Email already exists")
            return None
    
    def get_all_users(self):
        """Get all users"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, email, age, created_at FROM users')
            return cursor.fetchall()
    
    def get_user_by_id(self, user_id):
        """Get a single user by ID"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, email, age, created_at FROM users WHERE id = ?', (user_id,))
            return cursor.fetchone()
    
    def get_post_by_id(self, post_id):
        """Get a single post by ID"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, user_id, title, content, created_at FROM posts WHERE id = ?', (post_id,))
            return cursor.fetchone()
    
    def create_post(self, user_id, title, content):
        """Create a new post for a user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)',
                (user_id, title, content)
            )
            conn.commit()
            return cursor.lastrowid
    
    def get_user_posts(self, user_id):
        """Get all posts for a specific user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT id, title, content, created_at FROM posts WHERE user_id = ?',
                (user_id,)
            )
            return cursor.fetchall()
    
    def update_user(self, user_id, name=None, email=None, age=None):
        """Update a user's information"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Start building the UPDATE query
            updates = []
            values = []
            
            # Check which fields we need to update
            if name is not None:
                updates.append("name = ?")
                values.append(name)
            
            if email is not None:
                updates.append("email = ?")
                values.append(email)
            
            if age is not None:
                updates.append("age = ?")
                values.append(age)
            
            # If nothing to update, return False
            if not updates:
                print("No fields to update")
                return False
            
            # Add the user_id to the values list
            values.append(user_id)
            
            # Build the final query
            query = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
            
            try:
                cursor.execute(query, values)
                conn.commit()
                return cursor.rowcount > 0  # True if user was found and updated
            except sqlite3.IntegrityError:
                print("Error: Email already exists for another user")
                return False
    
    def update_post(self, post_id, title=None, content=None):
        """Update a post's title and/or content"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Start building the UPDATE query
            updates = []
            values = []
            
            # Check which fields we need to update
            if title is not None:
                updates.append("title = ?")
                values.append(title)
            
            if content is not None:
                updates.append("content = ?")
                values.append(content)
            
            # If nothing to update, return False
            if not updates:
                print("No fields to update")
                return False
            
            # Add the post_id to the values list
            values.append(post_id)
            
            # Build the final query
            query = f"UPDATE posts SET {', '.join(updates)} WHERE id = ?"
            
            cursor.execute(query, values)
            conn.commit()
            return cursor.rowcount > 0  # True if post was found and updated
    
    def delete_user(self, user_id):
        """Delete user and their posts"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM posts WHERE user_id = ?', (user_id,))
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            conn.commit()
            return cursor.rowcount > 0

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print(" DATABASE MANAGER")
    print("="*40)
    print("1. Create User")
    print("2. View All Users")
    print("3. Create Post")
    print("4. View User Posts")
    print("5. Update User")
    print("6. Update Post")
    print("7. Delete User")
    print("8. Exit")
    print("-"*40)

def main():
    """Main interactive CLI function"""
    db = DatabaseManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1':
            print("\n-- Create New User --")
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            try:
                age = int(input("Enter age: ").strip())
                user_id = db.create_user(name, email, age)
                if user_id:
                    print(f"✓ User created successfully! ID: {user_id}")
                else:
                    print("✗ Failed to create user")
            except ValueError:
                print("✗ Invalid age. Please enter a number.")
        
        elif choice == '2':
            print("\n-- All Users --")
            users = db.get_all_users()
            if users:
                print(f"{'ID':<5} {'Name':<20} {'Email':<30} {'Age':<5} {'Created At'}")
                print("-" * 80)
                for user in users:
                    print(f"{user[0]:<5} {user[1]:<20} {user[2]:<30} {user[3]:<5} {user[4]}")
            else:
                print("No users found.")
        
        elif choice == '3':
            print("\n-- Create New Post --")
            try:
                user_id = int(input("Enter user ID: ").strip())
                title = input("Enter post title: ").strip()
                content = input("Enter post content: ").strip()
                post_id = db.create_post(user_id, title, content)
                if post_id:
                    print(f"✓ Post created successfully! ID: {post_id}")
                else:
                    print("✗ Failed to create post")
            except ValueError:
                print("✗ Invalid user ID. Please enter a number.")
        
        elif choice == '4':
            print("\n-- View User Posts --")
            try:
                user_id = int(input("Enter user ID: ").strip())
                posts = db.get_user_posts(user_id)
                if posts:
                    print(f"Posts for User ID {user_id}:")
                    print(f"{'ID':<5} {'Title':<30} {'Content':<40} {'Created At'}")
                    print("-" * 85)
                    for post in posts:
                        print(f"{post[0]:<5} {post[1]:<30} {post[2]:<40} {post[3]}")
                else:
                    print(f"No posts found for user ID {user_id}")
            except ValueError:
                print("✗ Invalid user ID. Please enter a number.")
        
        elif choice == '5':  # UPDATE USER
            print("\n-- Update User --")
            try:
                user_id = int(input("Enter user ID to update: ").strip())
                
                # Check if the user exists
                user = db.get_user_by_id(user_id)
                if not user:
                    print(f"✗ User {user_id} not found")
                    continue
                
                # Show current user info
                print(f"\nCurrent user information:")
                print(f"Name: {user[1]}")
                print(f"Email: {user[2]}")
                print(f"Age: {user[3]}")
                
                print("\nLeave blank to keep current value")
                name = input("Enter new name (or press Enter to skip): ").strip()
                email = input("Enter new email (or press Enter to skip): ").strip()
                age_input = input("Enter new age (or press Enter to skip): ").strip()
                
                # Convert empty strings to None (meaning "don't update this field")
                name = name if name else None
                email = email if email else None
                age = int(age_input) if age_input else None
                
                if db.update_user(user_id, name, email, age):
                    print(f"✓ User {user_id} updated successfully!")
                else:
                    print(f"✗ Failed to update user {user_id}")
            except ValueError:
                print("✗ Invalid age. Please enter a number.")
        
        elif choice == '6':  # UPDATE POST
            print("\n-- Update Post --")
            try:
                post_id = int(input("Enter post ID to update: ").strip())
                
                # Check if the post exists
                post = db.get_post_by_id(post_id)
                if not post:
                    print(f"✗ Post {post_id} not found")
                    continue
                
                # Show current post info
                print(f"\nCurrent post information:")
                print(f"Title: {post[2]}")
                print(f"Content: {post[3]}")
                
                print("\nLeave blank to keep current value")
                title = input("Enter new title (or press Enter to skip): ").strip()
                content = input("Enter new content (or press Enter to skip): ").strip()
                
                # Convert empty strings to None (meaning "don't update this field")
                title = title if title else None
                content = content if content else None
                
                if db.update_post(post_id, title, content):
                    print(f"✓ Post {post_id} updated successfully!")
                else:
                    print(f"✗ Failed to update post {post_id}")
            except ValueError:
                print("✗ Invalid post ID. Please enter a number.")
        
        elif choice == '7':
            print("\n-- Delete User --")
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                confirm = input(f"Are you sure you want to delete user {user_id} and all their posts? (y/n): ").strip().lower()
                if confirm == 'y':
                    if db.delete_user(user_id):
                        print(f"✓ User {user_id} and their posts deleted successfully!")
                    else:
                        print(f"✗ User {user_id} not found")
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("✗ Invalid user ID. Please enter a number.")
        
        elif choice == '8':
            print("Goodbye!")
            break
        
        else:
            print("✗ Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()