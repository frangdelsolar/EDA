<h1>Quoridor Bot</h1>
by <strong>Francisco Javier González del Solar</strong>

<p>This project was created as a part of a challenge for the Eventbrite Development Academy held in May 2022.</p>

<h2>About the project</h2>
<p>The aim of the project was to create an Artificial Intelligence able to play a mod version of Quoridor developed by the EDA team.</p>
<p>The code has two distincts branches to hold logic for different algorithms to play the game.</p>

<h3>Base code</h3>
The base code consists of a series of classes and functions that serve the purpose of connecting with the socket and managing the state of the game. To that end, the bot
has a ConnectionManager that is capable of managing as many Challenges as the player is invited to participate. 
When the action 'your-turn' is sent by the server, the Challenge object decides whether it will play by moving a pawn on the board or placing a wall. This decision is 
based on a representation of the state of the game that analises the scores of the players according to the elements of the board.

<h3>Main branch</h3>

<p>On this branch, it is possible to configure the AI to play with two different approaches.</p>
<ol>
    <li>Choosing the shortest path towards the opposite end of the board.</li>
    <li>Choosing the best possible move, anticipating the best possible moves of the opponent</li>
</ol>

<h4>1. The Shortest Path - Breadth First Search Algorithm Implementation</h4>
<small><a href="https://en.wikipedia.org/wiki/Breadth-first_search">Breadth First Search</a> on Wikipedia.</small>
<p>As the board gets more complex by the movement of the pawns and the walls that are being built. The pawn faces the problem of getting towards the target position
using the shortest path possible. It is implemented a search algorithm that traverses the board looking for valid spots where the user could move, and accounts for the distance of the possible movements.</p>

<h4>2. Anticipation - Minimax Algorithm Implementation</h4>
<small><a href="https://en.wikipedia.org/wiki/Minimax">Minimax</a> on Wikipedia.</small>
<p>In order to decide the best possible move, this algorithm helps the game state manager decide anticipating the scores of the board given that all players choose to play the shortest way to the end of the board. It is configured to anticipate up to three moves of each player ahead.</p>

<p>However, this seemed to be the right approach to this problem. It faced performance issues. As every move took 3 secs on average to be decided.</p>

<h3>Minimax-no-bfs Branch</h3>

<p>To overcome the performance issues above mentioned, it was set this alternative to not anticipate the shortest path for each pawn, but assessing the score of the board for every possible move of every pawn on the board.</p>
<p>The result of this approach was better in performance, with only 1 second on average per move. Nevertheless, the final score of the AI was lower than using just the Shortest Path Algorithm.</p>

<h2>Testing</h2>
<a href='https://coveralls.io/github/frangdelsolar/EDA?branch=main'><img src='https://coveralls.io/repos/github/frangdelsolar/EDA/badge.svg?branch=main' alt='Coverage Status' /></a>
<p>As a part of the project, it was demanded to aim to the best test coverage possible.</p>
<p>I implemented a TDD policy to meet the highest score possible. It was a wise decision as it speed up the debugging process for the development of the most complex scenarios such as getting the valid moves for each pawn, calculating the score of the board, anticipating game states, and looking for the best moves to be done.</p>

<p>Following, there are some screenshots for the testing of the function get_valid_move for the pawns: </p>

![image](https://user-images.githubusercontent.com/54779433/169143711-09412c3f-1b48-40db-a259-603fb330ca71.png)

![image](https://user-images.githubusercontent.com/54779433/169143786-83d77437-abb3-4ac6-ba2c-955ce3b95f37.png)

![image](https://user-images.githubusercontent.com/54779433/169143888-88549ae8-561c-49a7-8fdb-8ac724af2398.png)


<p>These are two examples of the results of the BFS implementation.</p>

![image](https://user-images.githubusercontent.com/54779433/169144755-0c4e921c-2ca6-4d09-8aba-460045906930.png)

![image](https://user-images.githubusercontent.com/54779433/169144531-5c75582b-2643-4d22-b144-5731b8efe86e.png)



