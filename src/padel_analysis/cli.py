"""Command line interface for the padel analysis project."""

from __future__ import annotations

import argparse

from .models import Match, Team


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze a simple padel match summary.")
    parser.add_argument("--home", default="Home Team", help="Name of the home team.")
    parser.add_argument("--away", default="Away Team", help="Name of the away team.")
    parser.add_argument(
        "--score",
        nargs="*",
        default=["6-4", "7-5"],
        help="Set scores in home-away format, for example: 6-4 7-5",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    match = Match(
        home_team=Team(args.home),
        away_team=Team(args.away),
        set_scores=list(args.score),
    )
    print(match.summary())


if __name__ == "__main__":
    main()
