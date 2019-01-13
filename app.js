var     express     = require('express') ,
            say     = require('say'),
        mongoose    = require("mongoose"),
        bodyParser  = require("body-parser"),
        WaveFile    = require('wavefile'),
            User    = require('./models/user'),
            app     = express();
var port = process.env.port || 8083 ;
var methodOverride = require("method-override");

mongoose.connect("mongodb://localhost/blind" , { useNewUrlParser: true });
app.use(bodyParser.urlencoded({ extended: true }));
app.use(methodOverride("_method"));

//Method declarations
/* say.setPlatform(say.platforms.WIN32 || say.platforms.MACOS || say.platforms.LINUX)
say.speak(text, voice || null, speed || null, callback || null)
say.export(text, voice || null, speed || null, filename, callback || null) */


app.get('/api/:name' , (req,res)=> {
    var nameOfUser = req.params.name ;
    nameOfUser = nameOfUser.toLowerCase();
    // console.log(nameOfUser);
    var newUser = {
        name : nameOfUser
    }
    User.find({name : nameOfUser } , function(err , foundUser){
        
        if(foundUser.length == 0){
           console.log('User Not found so we will be making one');
           User.create(newUser , function(err , done){
            console.log('New user created');
            say.speak("Hey Unknown !" , 'Veena' , 1);
            });
        } else {
            console.log('USER FOUND');
            say.speak(nameOfUser + ' is infront of you!' , 'Veena' , 1);
            say.export(nameOfUser + ' is infront of you!' , 'Veena' , 1 , 'user.wav' , (err) => {
                if (err) {
                    return console.error(err)
                }
                
                console.log('Voice has been saved to user.wav.')
            })
        }
    })
    res.json({
        message : 'Yay ! User was detected' 
    })
})

app.get('/api/object/:object' , (req,res)=> {
    var newObject = req.params.object;
    say.speak(newObject + ' is infront of you! ', 'Veena' , 1);
    say.export(newObject + ' is infront of you!' , 'Veena' , 1 , 'object.wav' , (err) => {
        if (err) {
            return console.error(err)
        }
        console.log('Voice has been saved to object.wav.')
    })
    res.json({
        message : 'Yay! Object was detected'
    })
})

app.listen(port , () => {
    console.log('Server is running');
});