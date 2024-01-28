import typer
from pathlib import Path
from typing import Annotated, List


def create_symlink(
    src_path: Annotated[Path, typer.Option("--src", "-s")],
    dst_path: Annotated[Path, typer.Option("--dst", "-d")],
):
    dst_base = list(dst_path.parts)[0]
    src_files: List[Path] = [name for name in src_path.rglob("*") if name.is_file()]
    for src_file in src_files:
        dst = list(src_file.parts)
        dst[0] = dst_base
        dst = Path(*dst)
        dst.parent.mkdir(parents=True, exist_ok=True)
        if "cmake" in src_file.name.lower():
            dst.with_name("BUILD.bazel").touch(exist_ok=True)
            print(f"created empty file {dst.with_name('BUILD.bazel')}")
        elif "readme" in src_file.name.lower():
            dst.with_name("README.md").touch(exist_ok=True)
            print(f"created empty file {dst.with_name('README.md')}")
        else:
            if not dst.exists():
                print(f"creating symlink {dst}")
                dst.symlink_to(src_file.absolute())


if __name__ == "__main__":
    typer.run(create_symlink)
