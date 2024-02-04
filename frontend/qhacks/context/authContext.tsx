"use client";

import { getCsrfToken, getLogout, postLogin, postSignup } from "@/lib/utils";
import { createContext, useContext, useState, useEffect } from "react";

const AuthContext = createContext({});

export function useAuth() {
  return useContext(AuthContext);
}

export function AuthProvider({ children }: any) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [csfr, setCsfr] = useState(null);

  useEffect(() => {
    setLoading(false);
  }, []);

  const value = {
    user,
    loading,
    setUser,
  };

  useEffect(() => {
    const getToken = async () => {
      try {
        const val = await getCsrfToken();
        const userId = await postLogin("natlie@gmail.com", "123", val);

        // Store it in local storage
        localStorage.setItem("csrfToken", val);
        localStorage.setItem("userId", userId.data.user.user);
        console.log(val, userId);
        setCsfr(val);
        setUser(userId.data.user);
      } catch (e) {
        alert("error with login");
      }
    };

    getToken();
  }, []);

  return (
    <AuthContext.Provider value={value}>
      {!loading && children}
    </AuthContext.Provider>
  );
}
