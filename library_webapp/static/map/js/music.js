export default class Music{
    constructor(title, genre, duration){
        this.title = title
        this.genre = genre
        this.duration = duration
    }

}

export function printMusic(music){
    console.log(music.title +": " +music.duration)
}