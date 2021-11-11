import React from "react";

const Login = () => {
  return (
    <div>
      <form>
        <input
          type="text"
          placeholder="Enter Username"
          name="username"
          defaultValue=""
          required
        />
        <br />
        <input
          type="password"
          placeholder="Enter Password"
          name="password"
          defaultValue=""
          required
        />
        <br />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;
