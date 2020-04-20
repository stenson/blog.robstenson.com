import markdown, jinja2, frontmatter
from pathlib import Path
from shutil import copytree
from time import time
from datetime import datetime


postsdir = Path("posts")
posts = []

for post in reversed(sorted(postsdir.glob("*.md"))):
    _post = frontmatter.loads(post.read_text())
    _post.content = markdown.markdown(_post.content, extensions=["smarty", "mdx_linkify"])
    posts.append([post.stem, _post])

print([p[0] for p in posts])

build_time = datetime.utcfromtimestamp(int(time())).strftime("%a, %d %b %Y %H:%M:%S %z")

env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
index_template = env.get_template("index.j2")
feed_template = env.get_template("feed.j2")
post_template = env.get_template("post.j2")

sitedir = Path("_site")
sitedir.mkdir(exist_ok=True)

copytree(Path("assets"), sitedir / "assets", dirs_exist_ok=True)
(sitedir / "index.html").write_text(index_template.render(dict(posts=posts)))
(sitedir / "feed.xml").write_text(feed_template.render(dict(build=build_time, posts=posts)))
(sitedir / "posts").mkdir(exist_ok=True)

for post in posts:
    (sitedir / f"posts/{post[0]}.html").write_text(post_template.render(dict(post=post)))
