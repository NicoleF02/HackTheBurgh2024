export class Banana {
    constructor(game) {
        this.game = game;
        this.width = 16;
        this.height = 16;
        this.x = Math.random() * this.game.width;
        this.y = Math.random() * this.game.height;
        this.image = document.getElementById('banana');
    }
    draw(context){
        context.drawImage(this.image, 0, 0, this.width, this.height, this.x, this.y, this.width, this.height);
    }
}