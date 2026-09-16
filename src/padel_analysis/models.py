"""Core data models for padel match analysis."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Player:
    """Represents a single padel player."""

    name: str
    points: int = 0
    aces: int = 0
    double_faults: int = 0
    winners: int = 0
    unforced_errors: int = 0


@dataclass
class Team:
    """Represents a team of one or more players."""

    name: str
    players: list[Player] = field(default_factory=list)

    @property
    def total_points(self) -> int:
        return sum(player.points for player in self.players)

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def summary(self) -> str:
        player_names = ", ".join(player.name for player in self.players) or "No players"
        return f"{self.name} ({player_names})"


@dataclass
class Match:
    """Representation of a completed padel match."""

    home_team: Team
    away_team: Team
    set_scores: list[str] = field(default_factory=list)

    @property
    def winner(self) -> str:
        home_wins = 0
        away_wins = 0

        for set_score in self.set_scores:
            try:
                home_score, away_score = (int(part.strip()) for part in set_score.split("-"))
            except ValueError:
                continue
            if home_score > away_score:
                home_wins += 1
            elif away_score > home_score:
                away_wins += 1

        if home_wins > away_wins:
            return self.home_team.name
        if away_wins > home_wins:
            return self.away_team.name
        return "Draw"

    def summary(self) -> str:
        scoreline = " ".join(self.set_scores) if self.set_scores else "No completed sets"
        return f"{self.home_team.name} vs {self.away_team.name}: {scoreline}. Winner: {self.winner}"
