from __future__ import annotations

import sys
from pathlib import Path

from book_meta import (
    chapter_paths,
    load_meta,
    normalize_readme,
    replace_top_heading_with_latex,
    resolve_book_dir,
    short_title_for_path,
    strip_local_file_links,
)


def build_book(book_dir: Path, meta: dict) -> str:
    readme_path = meta.get("readme_path", "README.md")
    chunks: list[str] = []
    for md_path in chapter_paths(book_dir):
        path = book_dir / md_path
        text = path.read_text(encoding="utf-8").strip()
        if md_path == readme_path:
            text = normalize_readme(
                text,
                title=meta["title"],
                cover_alt=meta.get("cover_alt"),
            )
        else:
            short_title = short_title_for_path(md_path, text)
            if short_title:
                text = replace_top_heading_with_latex(
                    text,
                    short_title=short_title,
                )
        text = strip_local_file_links(text)
        chunks.append(text)

    return "\n\n\\clearpage\n\n".join(chunks) + "\n"


def main() -> None:
    book_dir = resolve_book_dir(sys.argv[1] if len(sys.argv) > 1 else None)
    meta = load_meta(book_dir)
    output = book_dir / "_book" / "book.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_book(book_dir, meta), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
