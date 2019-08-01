import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Board from './Board'

function App() {

  const [solving, setSolving] = useState(false)
  const [tiles, setTiles] = useState([]);
  const [actions, setActions] = useState([])


  const fetchRandomBoard = () => {
    axios(
      'http://localhost:5000/random-board'
    )
      .then(data => {
        setTiles(data.data.board)
        setActions([])
      });
  }

  const solveBoard = () => {
    setSolving(true)
    axios.post('http://localhost:5000/solve-board', {
      'state': tiles
    }).then(data => {
      setActions(data.data.actions)
    })
  }

  useEffect(() => {
    setSolving(false)
    fetchRandomBoard()
  }, []);

  console.log(solving)

  return (
    <div>
      <Board
        tiles={tiles}
        actions={actions}
        isSolving={solving}
        setSolving={setSolving.bind(this)}
        setTiles={setTiles.bind(this)}        
      />
      <div>
        <button onClick={() => {
          fetchRandomBoard()
        }}>
          randomise
        </button>
        <button onClick={() => {
          solveBoard()
        }}>
          solve
        </button>
      </div>
    </div>
  );
}

export default App;