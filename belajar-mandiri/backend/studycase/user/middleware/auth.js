
const auth = async (req) =>{
    const headers = req.headers
    if(headers["auth-id"] == "90924090204"){
        return true
    }else{
        return false
    }

}

export default auth