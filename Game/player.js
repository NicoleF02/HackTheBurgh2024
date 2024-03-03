export class Player {
    constructor(game, inputSet) {
        this.game = game;
        this.inputSet = inputSet;
        this.width = 32;
        this.height = 32;
        this.x = 0;
        this.y = this.game.height - this.height;
        this.vy = 0;
        this.weight = 1;
        this.image = document.getElementById('player');
        this.speed = 0;
        this.maxSpeed = 10;
    }
    update(input) {
        //Horizontal Movement
        this.x += this.speed;
        if (input.includes(this.inputSet[1])) this.speed = this.maxSpeed;
        else if (input.includes(this.inputSet[2])) this.speed = -this.maxSpeed;
        else this.speed = 0;
        if (this.x < 0) this.x = 0;
        if (this.x > this.game.width - this.width) this.x = this.game.width - this.width;
        //Vertical Movement
        if (input.includes(this.inputSet[0]) && this.onGround()) this.vy = -30;
        this.y += this.vy;
        if (!this.onGround()) this.vy += this.weight;
        else this.vy = 0;
    }
    draw(context){
        context.drawImage(this.image, 0, 0, this.width, this.height, this.x, this.y, this.width, this.height);
    }
    onGround(){
        return this.y === this.game.height - this.height;
    }
}