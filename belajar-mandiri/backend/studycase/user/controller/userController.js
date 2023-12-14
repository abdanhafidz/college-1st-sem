import createUserService from '../services/createUserService.js'
import getUserInfoService from '../services/getUserInfoService.js'
import loginUserService from '../services/loginUserService.js'
class userController{
    createUser(req,res){
        return createUserService(req,res)
    }
    getUserInfo(req,res){
        return getUserInfoService(req,res)
    }
    loginUser(req,res){
        return loginUserService(req,res)
    }
}

export default userController