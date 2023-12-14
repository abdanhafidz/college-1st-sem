import userController from "../controller/userController.js";
import { Router } from "express"

const userRouter = Router()
const userControll = new userController

userRouter.post("/create",(req,res) => {
    res.send(userControll.createUser(req,res))
});

userRouter.get("/whois",(req,res) => {
    res.send(userControll.getUserInfo(req,res))
});

userRouter.post("/login",(req,res) => {
    res.send(userControll.loginUser(req,res))
});

export default userRouter