class World{
    constructor(){
        this.row = 10;
        this.col = 10;
        this.pit = 1;
        this.wumpus = 2;
        this.gold = 3;
        this.createWorld();
        this.createEnemiesAndGold();
    }

    createWorld(){

       for(let i=0; i<10; i++){
           for(let j=0; j<10; j++){
                let htmlString = `<div class = "cell indx${i}${j}"><span class = "txt${i}${j}">.</span></div>`;
                $(`.row${i}`).append(htmlString);
           }           
       }
       $(".indx00").addClass("man-right");
       $(".indx00").addClass("visited");


    }

    createEnemiesAndGold(){

        let rowOccupied = [];
        let colOccupied = [];

        for(let i=0; i<12; i++){
            let row = Math.floor(Math.random() * 10);
            let col = Math.floor(Math.random() * 10);

            if(row == 0 && col == 0){
                i--;
                continue;
            }

            if(rowOccupied.includes(row) && colOccupied.includes(col)) {
                i--;
                continue;
            }


            if(i==10){
                $(`.indx${row}${col}`).addClass("gold");
                continue;

            }
            else if(i==11){
                $(`.indx${row}${col}`).addClass("wumpus");
                continue;
            }

            rowOccupied.push(row);
            colOccupied.push(col);

            $(`.indx${row}${col}`).addClass("pit");

            

        }


        console.log(rowOccupied.length);
        console.log(colOccupied.length);
  
    }
}

class Control{
    constructor(world){
        this.world = world;
        this.up ="ArrowUp";
        this.down ="ArrowDown";
        this.left ="ArrowLeft";
        this.right ="ArrowRight";

        this.handleEvents();
    }

    handleEvents(){
        let that = this;

        window.addEventListener("keydown", function(e) {
            if([32, 37, 38, 39, 40].indexOf(e.keyCode) > -1) {
                e.preventDefault();
            }
        }, false);

        $(document).on("keydown", function(e){
            if(e.code == that.up) {
                $(".indx00").addClass("man-up");
                $(".indx00").removeClass("man-down");
                $(".indx00").removeClass("man-left");
                $(".indx00").removeClass("man-right");
                
            
            }
            else if(e.code == that.down){
                $(".indx00").addClass("man-down");
                $(".indx00").removeClass("man-up");
                $(".indx00").removeClass("man-left");
                $(".indx00").removeClass("man-right");
            } 
            else if(e.code == that.left){
                $(".indx00").addClass("man-left");
                $(".indx00").removeClass("man-down");
                $(".indx00").removeClass("man-up");
                $(".indx00").removeClass("man-right");
            } 
            else if(e.code == that.right){
                $(".indx00").addClass("man-right");
                $(".indx00").removeClass("man-down");
                $(".indx00").removeClass("man-left");
                $(".indx00").removeClass("man-up");
            } 
        })

    }
}

$(document).ready(function(){
    let world = new World();
    let control  = new Control(world)

   
   
})