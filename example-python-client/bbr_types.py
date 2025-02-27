from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime
from uuid import UUID

# This is generated by Claude.ai, no human has read this code!

@dataclass
class ExchangeMapEntry:
    cropSize: int
    value: int

@dataclass
class CardDto:
    id: UUID
    type: str
    exchangeMap: List[ExchangeMapEntry]

@dataclass
class FieldDto:
    key: UUID
    card: List[CardDto]

@dataclass
class HandCardDto:
    firstCard: bool
    id: UUID
    type: str
    exchangeMap: List[ExchangeMapEntry]

@dataclass
class TradeDto:
    initiatorId: UUID
    negotiationId: UUID
    offeredCards: List[str]
    cardTypesWanted: List[str]

@dataclass
class PlayerDto:
    name: str
    coins: int
    fields: List[FieldDto]
    hand: int
    drawnCards: List[CardDto]
    tradedCards: List[CardDto]
    isActive: bool

@dataclass
class GameStateDto:
    name: str
    currentPlayer: str
    currentPhase: str
    currentState: str
    round: int
    phaseTimeLeft: str
    phaseEndTimestamp: datetime
    lastStateChange: datetime
    deck: int
    availableTrades: List[TradeDto]
    discardPile: List[any]
    players: List[PlayerDto]
    yourHand: List[HandCardDto]

@dataclass
class OfferDto:
    offeredCards: List[UUID]
    cardTypesWanted: List[str]

@dataclass
class AcceptDto:
    negotiationId: UUID
    payment: List[UUID]

@dataclass
class ErrorResponse:
    message: str
