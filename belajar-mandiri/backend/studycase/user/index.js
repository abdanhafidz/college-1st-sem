
import express from "express"
import userRouter from './routes/userRouter.js';
const app = express()
app.use(express.json());
app.use("/user",userRouter)

app.listen(8900,()=>{
    console.log("Listening on 8900 port")
});