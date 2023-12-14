import dataUser from '../database/dataUser.js'

const getUserInfoService = async(req,res)=> {
    const username = req.body.username
    return dataUser.filter((user) => user.username == username)
}

export default getUserInfoService