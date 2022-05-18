<h1>Quoridor Bot</h1>
by <strong>Francisco Javier González del Solar</strong>

<p>This project was created as a part of a challenge for Eventbrite Development Academy held in May 2022.</p>

<h2>About the project</h2>
<p>The aim of the project was to create an Artificial Intelligence able to play a mod version of Quoridor developed by the EDA team.</p>
<p>The code has two distincts branches to hold logic for different algorithms to play the game.</p>

<h3>Base code</h3>
The base code consists of a series of classes and functions that serve the purpose of connecting with the socket and managing the state of the game. To that end, the bot
has a ConnectionManager that is capable of managing as many Challenges as the player is invited to participate. 
When the action 'your-turn' is sent by the server, the Challenge object decides whether it will play by moving a pawn on the board or placing a wall. This decision is 
based on a representation of the state of the game that analises the scores of the players according to the elements of the board.

<h3>Main branch</h3>

<p></p>

<h3>Minimax-no-bfs Branch</h3>

<p></p>

<h2>Testing</h2>
<a href='https://coveralls.io/github/frangdelsolar/EDA?branch=main'><img src='https://coveralls.io/repos/github/frangdelsolar/EDA/badge.svg?branch=main' alt='Coverage Status' /></a>
