import sqlite3

class DatabaseManager:
    def __init__(self, db_name='example.db'):
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
    print("5. Delete User")
    print("6. Exit")
    print("-"*40)


def main():
    """Main interactive CLI function"""
    db = DatabaseManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
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
        
        elif choice == '5':
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
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("✗ Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()