// Access HTML elements
let doorImage1 = document.getElementById('door1');
let doorImage2 = document.getElementById('door2');
let doorImage3 = document.getElementById('door3');
let startButton = document.getElementById('start');

let botDoorPath = './public/images/robot.svg';
let beachDoorPath = './public/images/beach.svg';
let spaceDoorPath = './public/images/space.svg';
let closedDoorPath = './public/images/closed_door.svg';

let numClosedDoors = 3;
let openDoor1;
let openDoor2;
let openDoor3;
let currentlyPlaying = true;

// Define game logic to check doors, progress game, end game, and choose a random chore door
const isClicked = (door) => {
    if (door.src.endsWith('closed_door.svg')) {
        return true
    } else {
        return false
    }
}

const isBot = (door) => {
    if (door.src.endsWith('robot.svg')) {
        return true
    } else {
        return false
    }
}

const gameOver = (status) => {
    if (status === 'win') {
        startButton.innerHTML = 'You win! Play again?'
    } else {
        startButton.innerHTML = 'Game over! Play again?'
    }
    currentlyPlaying = false
}

const playDoor = (door) => {
    numClosedDoors--
    if (numClosedDoors === 0) {
        gameOver('win')
    } else if (isBot(door)) {
        gameOver('')
    }
}

const randomChoreDoorGenerator = (door) => {
    let choreDoor = Math.floor(Math.random() * numClosedDoors)
    if (choreDoor === 0) {
        openDoor1 = botDoorPath
        openDoor2 = beachDoorPath
        openDoor3 = spaceDoorPath
    } else if (choreDoor === 1) {
        openDoor1 = beachDoorPath
        openDoor2 = botDoorPath
        openDoor3 = spaceDoorPath
    } else {
        openDoor1 = spaceDoorPath
        openDoor2 = beachDoorPath
        openDoor3 = botDoorPath
    }
}

doorImage1.onclick = () => {
    if (currentlyPlaying && isClicked(doorImage1)) {
        doorImage1.src = openDoor1;
        playDoor(doorImage1);
    }
}

doorImage2.onclick = () => {
    if (currentlyPlaying && isClicked(doorImage2)) {
        doorImage2.src = openDoor2;
        playDoor(doorImage2);
    }
}

doorImage3.onclick = () => {
    if (currentlyPlaying && isClicked(doorImage3)) {
        doorImage3.src = openDoor3;
        playDoor(doorImage3);
    }
}

startButton.onclick = () => {
    if (currentlyPlaying === false) {
        startRound();
    }
}

// Start a game round
const startRound = () => {
    doorImage1.src = closedDoorPath
    doorImage2.src = closedDoorPath
    doorImage3.src = closedDoorPath
    numClosedDoors = 3
    currentlyPlaying = true
    startButton.innerHTML = 'Good Luck!'
    randomChoreDoorGenerator()
}

startRound()