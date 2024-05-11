let ampm=document.getElementById('ampm')
function displaytime(){
    let time=new Date()
    let hrs=time.getHours();
    let min=time.getMinutes();
    let sec=time.getSeconds();
    if (hrs>12){
        hrs=hrs-12
        ampm.innerHTML="PM";
    }
    document.getElementById('hours').innerHTML=zero(hrs)
    document.getElementById('min').innerHTML=zero(min)
    document.getElementById('sec').innerHTML=zero(sec)
    
}
function zero(num){
    return num<10?'0'+num:num
}


setInterval(displaytime,500)