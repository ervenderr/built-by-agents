# What Is SQL Injection? Explained in 20 Seconds

Angle: a character types a trick into a login box and the database runs it as a command instead of text.

## Script

A login box can let a stranger read your database.
The trick is typing SQL code instead of a username.
A careless app glues that text into its query.
So the database runs it as a command, not as text.
That can read or change data, even log you in without the password.
Parameterized queries fix it by keeping input as data, never code.

## Voice
VoiceStudio BuiltByAgents, seed 42.

## Unverified
- Facts rely on SOURCES.md / facts.json; not re-checked here.
- Rows and the payload `' OR '1'='1` are illustrative (labelled ILLUSTRATIVE DATA); real apps vary.
- Visual check was via snapshots only; the render was not watched end to end.
