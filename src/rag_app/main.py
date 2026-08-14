from pathlib import Path
import argparse
from .knowledge_base import (
    build_knowledge_base,
    query_knowledge_base,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="RAG knowledge base command line tool"
    )

    parser.add_argument(
        "command",
        choices=["build", "query"],
        help="执行 build 构建知识库，或 query 查询知识库",
    )

    parser.add_argument(
        "query",
        nargs="?",
        help="查询问题，仅 query 模式需要",
    )

    args = parser.parse_args()

    if args.command == "build":
        build_knowledge_base()

    elif args.command == "query":
        if not args.query:
            parser.error(
                "query 模式需要提供查询问题"
            )

        answer = query_knowledge_base(
        args.query,
        )

        print("最终回答：")
        print(answer)

if __name__ == "__main__":
    main()