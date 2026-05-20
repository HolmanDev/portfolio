import os
import json

def generate_posts_registry():
    posts_dir = os.path.join(os.path.dirname(__file__), 'posts')
    
    # Create posts directory if it doesn't exist
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)
        print(f"Created directory: {posts_dir}")
    
    # Find all .md files
    markdown_files = [f for f in os.listdir(posts_dir) if f.endswith('.md')]
    markdown_files.sort()
    
    # Generate JSON registry
    registry_path = os.path.join(posts_dir, 'posts.json')
    with open(registry_path, 'w', encoding='utf-8') as f:
        json.dump(markdown_files, f, indent=2)
    print(f"Generated registry: {registry_path}")
        
    # Generate JS bundled data (to avoid CORS/fetch issues on file:// protocol)
    bundled_posts = []
    for fn in markdown_files:
        post_path = os.path.join(posts_dir, fn)
        try:
            with open(post_path, 'r', encoding='utf-8') as f:
                content = f.read()
            bundled_posts.append({
                "filename": fn,
                "content": content
            })
        except Exception as e:
            print(f"Error reading {fn}: {e}")
            
    js_data_path = os.path.join(posts_dir, 'posts_data.js')
    with open(js_data_path, 'w', encoding='utf-8') as f:
        f.write("// Auto-generated file. Do not edit directly.\n")
        f.write("window.BLOG_POSTS_DATA = ")
        json.dump(bundled_posts, f, indent=2)
        f.write(";\n")
    print(f"Generated JS bundle: {js_data_path}")

if __name__ == '__main__':
    generate_posts_registry()
