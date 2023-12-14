const data = {
    name: "abdan hafidz",
    bitches: 0,
};
const Headers = {
    "Content-Type": "application/json",
}
fetch('http://localhost:3000/users/post', {
    method: "POST",
    headers: Headers,
    body: JSON.stringify(data),
})
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
    });
