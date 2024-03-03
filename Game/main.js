import { Player } from './player.js';
import { InputHandler } from './input.js';

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
            this.player = new Player(this, player1);
            this.player2 = new Player(this, player2);
            this.input = new InputHandler();
        }
        update() {
            this.player.update(this.input.keys);
            this.player2.update(this.input.keys);
        }
        draw(context) {
            this.player.draw(context);
            this.player2.draw(context);
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