# Adenium game data

Lineage II (HighFive) tables, icons and map tiles for [Adenium](../Adenium), a bot for that game. The program needs them and does not ship them.

**These files are not covered by Adenium's MIT licence.** They come from Lineage II, which belongs to NCSOFT Corporation; "Lineage" and "Lineage II" are
trademarks of NCSOFT Corporation. Adenium and this package are not affiliated with NCSOFT. They are provided so that the program can show names and
pictures for a game you play. If you hold rights to any of it and want it removed, write to **adenium@atomicmail.io** and it will be taken down.

## Install

Copy the `DataFiles/`, `Icons/` and `Maps/` folders into Adenium's `data/` folder and merge them with what is there (`data/Scripts/` and the web files in
`data/DataFiles/` stay):

```
cp -r DataFiles Icons Maps /path/to/Adenium/data/
```

## What is in it

| Folder / file | Content | Where it comes from |
|---|---|---|
| `DataFiles/*.ini` | item, skill, NPC, recipe, augment, system-message and string tables; instance and server names | `SysString.ini` was decoded from the client's `sysstring-e.dat`; the origin of the others is not documented in detail, and the item and skill stat columns come from a game server's data (not in the client) |
| `DataFiles/maps.txt` | which map picture covers which world block and height range | origin not documented |
| `Icons/*.png` (7,364) | 32x32 item, skill and action icons | taken from the client's `Icon.utx`; five (`0`, `action_pledge_invite`, `action_pledge_leave`, `action_pledgeacademy_invite`, `$$$_mailbox`) are the program's own action icons whose origin is not documented |
| `Icons/aliases.txt` | 312 `name=target` lines: icon names a server uses for its own copy of a client icon (`00_vesper noble breastplate` is `armor_t94_u_i01`) | pixel comparison against the client's icons, checked by eye |
| `Maps/*.jpg` (272) | 900x900 world map tiles named `<x>_<y>.jpg` (or `<x>_<y>_<n>.jpg` for a second height range) | the community map collections of [l2walker](https://code.google.com/archive/p/l2walker) (251 of the tiles are pixel-identical to its `data/maps`) and [L2Net](https://github.com/hyperthermya/L2Net) (5 more match its `GameData/maps`); the other 16 tiles match neither and their origin is not documented |

Icons that only a custom server draws (cash-shop and event icons with no client counterpart) are not included; the program shows its `0.png` instead.
