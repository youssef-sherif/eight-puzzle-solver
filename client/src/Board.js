import React from 'react';
import './Board.css'

function Board(props) {

    const updateBoard = (i, arr) => {
        console.log(props.actions.length)        
        let index = props.tiles.findIndex(x => x === 0)
        let x, y = 0
        if (props.actions[i] === 'up') {
            console.log('up')
            x = index
            y = index - 3
            let temp = arr[x]
            arr[x] = arr[y]
            arr[y] = temp
        } else if (props.actions[i] === 'left') {
            console.log('left')
            x = index
            y = index - 1
            let temp = arr[x]
            arr[x] = arr[y]
            arr[y] = temp
        } else if (props.actions[i] === 'right') {
            console.log('right')
            x = index
            y = index + 1
            let temp = arr[x]
            arr[x] = arr[y]
            arr[y] = temp
        } else if (props.actions[i] === 'down') {
            console.log('down')
            x = index
            y = index + 3
            let temp = arr[x]
            arr[x] = arr[y]
            arr[y] = temp
        }        
    }

    if (props.isSolving) {
        let arr = Object.assign([], props.tiles)
        const update = async (i, arr) => {                        
            await updateBoard(i, arr)            
        }
        for (let i = 0; i < props.actions.length; i++) {
            update().then(() => {
                
            })
        }        

        props.setSolving(false)        
    }

    let i = 0
    return (
        <div className="wrapper">

            {props.tiles.map((tile) => {
                return (
                    <div key={i++}>
                        {tile}
                    </div>
                )
            })}
        </div>
    );
}

export default Board;