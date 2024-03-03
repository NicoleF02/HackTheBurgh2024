import { Player } from './player.js';
import { InputHandler } from './input.js';
import { Banana } from './banana.js';

window.addEventListener('load', function(){
    const canvas = document.getElementById('canvas1');
    const ctx = canvas.getContext("2d");
    canvas.width = 1500;
    canvas.height = 500;
    const player1 = ['ArrowUp', 'ArrowRight', 'ArrowLeft'];
    const player2 = ['w', 'd', 'a'];

    class Game {
        constructor(width, height) {
            this.width = width;
            this.height = height;
            this.banana = new Banana(this);
            this.pear = new Banana(this);
            this.player = new Player(this, player1);
            this.player2 = new Player(this, player2);
            this.input = new InputHandler();
            this.p1Win = false;
            this.p2Win = false;
        }
        update() {
            this.player.update(this.input.keys);
            this.player2.update(this.input.keys);
            if (this.banana.x < this.player.x + this.player.width &&
                 this.banana.x + this.banana.width > this.player.x &&
                 this.banana.y < this.player.y + this.player.height &&
                 this.banana.y + this.banana.height > this.player.y) {
                this.p1Win = true;
            }
            if (this.pear.x < this.player2.x + this.player2.width &&
                 this.pear.x + this.pear.width > this.player2.x &&
                 this.pear.y < this.player2.y + this.player2.height &&
                 this.pear.y + this.pear.height > this.player2.y) {
                this.p2Win = true;
            }
        }
        draw(context) {
            this.player.draw(context);
            this.player2.draw(context);
            this.banana.draw(context);
            this.pear.draw(context);
            if (this.p1Win && this.p2Win) {
                context.clearRect(0, 0, canvas.width, canvas.height);
                context.font = '30px Arial';
                context.fillText('Byte the Banana', this.game.width * 0.5, this.game.height * 0.5);
            }
        }
    }

    const game = new Game(canvas.width, canvas.height);
    console.log(game);

    function animate(){
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        game.update();
        game.draw(ctx);
        requestAnimationFrame(animate);
    }
    animate();
});