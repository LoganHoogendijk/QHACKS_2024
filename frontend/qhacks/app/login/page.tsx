"use client";
import React, { useState } from "react";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { cn, postLogin, postSignup } from "@/lib/utils";
import { outfit } from "@/lib/fonts";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Button } from "@/components/ui/button";
import { useAuth } from "@/context/authContext";
import { useRouter } from "next/navigation";

function page() {
  const router = useRouter();
  const [currTab, setCurrTab] = useState("login");

  const [loginUsername, setLoginUsername] = useState("");
  const [loginPassword, setLoginPassword] = useState("");

  const [signupUsername, setSignupUsername] = useState("");
  const [signupPassword, setSignupPassword] = useState("");
  const [signupRetypePassword, setSignupRetypePassword] = useState("");

  const handleTabChange = (value: any) => {
    console.log(value);
    setCurrTab(value);
  };
  const { csrf, setUser } = useAuth();

  const handleLogin = async () => {
    if (currTab === "login") {
      const res = postLogin(loginUsername, loginPassword, csrf);
      router.push("/plants");
    }
  };

  const handleSignUp = async () => {
    console.log("fdsajfsdjlk");
    if (signupPassword !== signupRetypePassword) {
      alert("Passwords don't match");
    }

    if (currTab === "signup") {
      const res = await postSignup(signupUsername, signupPassword, csrf);
      const data = res.data;
      setUser({ id: data.user });

      router.push("/plants");
    }
  };
  return (
    <div className="flex justify-center items-center min-h-[100vh] z-[11] relative">
      <div className="flex justify-center items-start w-[500px] min-h-[500px]">
        <Tabs
          defaultValue="login"
          className=" w-[100%]"
          onValueChange={handleTabChange}
        >
          <TabsList className="grid w-full grid-cols-2">
            <TabsTrigger value="login">Login</TabsTrigger>
            <TabsTrigger value="signup">Sign-Up</TabsTrigger>
          </TabsList>
          <TabsContent value="login">
            <Card>
              <CardHeader>
                <CardTitle className="font-[400] text-[#6c6c6c] text-subheading">
                  Welcome Back
                </CardTitle>
                <CardDescription>
                  Let's continue to make our plants healthy.
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-2">
                <div className="space-y-1">
                  <Label htmlFor="username" className="text-body">
                    Username
                  </Label>
                  <Input
                    id="username"
                    value={loginUsername}
                    onChange={(e) => setLoginUsername(e.target.value)}
                    defaultValue=""
                  />
                </div>
                <div className="space-y-1">
                  <Label htmlFor="password" className="text-body">
                    Password
                  </Label>
                  <Input
                    id="password"
                    type="password"
                    defaultValue=""
                    value={loginPassword}
                    onChange={(e) => setLoginPassword(e.target.value)}
                  />
                </div>
              </CardContent>
              <CardFooter>
                <Button
                  className=" min-w-[120px]"
                  onClick={() => handleLogin()}
                >
                  Login
                </Button>
              </CardFooter>
            </Card>
          </TabsContent>
          <TabsContent value="signup">
            <Card>
              <CardHeader>
                <CardTitle className="font-[400] text-mutedText text-subheading">
                  Sign-Up
                </CardTitle>
                <CardDescription>
                  Let's start keeping things healthy.
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-2">
                <div className="space-y-1">
                  <Label htmlFor="username" className="">
                    Username
                  </Label>
                  <Input
                    id="username"
                    defaultValue=""
                    value={signupUsername}
                    onChange={(e) => setSignupUsername(e.target.value)}
                  />
                </div>
                <div className="space-y-1">
                  <Label htmlFor="new" className="">
                    Retype Password
                  </Label>
                  <Input
                    id="new"
                    type="password"
                    value={signupPassword}
                    onChange={(e) => setSignupPassword(e.target.value)}
                  />
                </div>
                <div className="space-y-1">
                  <Label htmlFor="new" className="">
                    Retype Password
                  </Label>
                  <Input
                    id="new"
                    type="password"
                    value={signupRetypePassword}
                    onChange={(e) => setSignupRetypePassword(e.target.value)}
                  />
                </div>
              </CardContent>
              <CardFooter>
                <Button onClick={() => handleSignUp()}>Sign Up</Button>
              </CardFooter>
            </Card>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
}

export default page;
