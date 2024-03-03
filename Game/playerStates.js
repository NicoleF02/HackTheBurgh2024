const states = {
    SITTING: 0,
    RUNNING: 1,
    JUMPING: 2,
}

class State {
    constructor(state){
        this.state = state;
    }
}

export class Sitting extends State {
    constructor(player){
        super(SITTING);
        this.player = player;
    }
    enter(){
        
    }
    handleInput(input){
        if (input.includes('ArrowUp')) this.player.setState(new Jumping(this.player));
        if (input.includes('ArrowRight') || input.includes('ArrowLeft')) this.player.setState(new Running(this.player));
    }
}