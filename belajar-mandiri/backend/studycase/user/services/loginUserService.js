import dataUser from '../database/dataUser.js'
import auth from '../middleware/auth.js'
import md5 from 'md5'

const loginUserService = async (req,res) =>{
    const username = req.body.username
    const password = req.body.password
    if(auth(req)){
        if(username == dataUser.username && password == md5(dataUser.password) ){
            return "Login Success!"
        }else{
            return "Account doesn't exist"
        }
    }else{
        return "Authentication failed"
    }
}

export default loginUserService