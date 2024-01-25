let place_name = document.getElementById("city")
let button = document.getElementById("search")



button.addEventListener("click",async () =>{

let place = place_name.value;
p = fetch(`http://api.openweathermap.org/geo/1.0/direct?q=${place}&appid=8a301729002ef55b2b877d24307dc509`)

p.then((response)=>{
    return response.json()

})
.then((response)=> {console.log(response)
    if (response.length == 0){
        document.body.style.backgroundImage = "url(assests/error.jpeg)"


    }

    else {
        document.body.style.backgroundImage = "url(assests/mount.jpg)"
    }
    
    let name = response[0].name
     let lat = response[0].lat
     let long = response[0].lon
     document.getElementById("name").innerText = name
    
    q = fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${long}&appid=8a301729002ef55b2b877d24307dc509`)
    q.then((got) => {
        return got.json()
    })
    .then((got)=> {console.log(got.weather[0].description)
        let tem = got.main.temp -273.15
        let desc = got.weather[0].description
        document.getElementById("tem").innerText = Math.round(tem) 
        document.getElementById("desc").innerText = desc
        let feel = got.main.feels_like
        document.getElementById("feel").innerText = `feels like ${Math.round(feel - 273.15)}`
        console.log(got)
        let imageObjectUrl = `https://openweathermap.org/img/wn/${got.weather[0].icon}@2x.png`
        document.getElementById("show").src = imageObjectUrl
        

        
    })


})


})



