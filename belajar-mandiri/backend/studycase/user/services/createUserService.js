import dataUser from '../database/dataUser.js'
import md5 from 'md5'

const createUserService = async (req,res) => {
    const name = req.body.name
    const username = req.body.username
    const password = req.body.password

    dataUser.push([
        {
            name:name,
            username:username,
            password:md5(password)
        }
    ])
    return "heyhey"
}

export default createUserService;