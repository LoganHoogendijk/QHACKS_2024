"use client";
import PlantsList from "@/components/plants/plantsList";
import Margins from "@/components/margins";
import React, { useEffect } from "react";
import Snapshot from "@/components/snapshot/snapshot";
import { useData } from "@/context/dataContext";
import { userProfile } from "@/lib/utils";
import { useAuth } from "@/context/authContext";

function Plants() {

  return (
    <div className="h-[100vh] w-[100%]">
      <Margins className="flex justify-start items-center mt-[100px]  flex-col">
        <h1 className="text-heading text-themeBtns">Your Garden</h1>
        <PlantsList />
      </Margins>
      <Snapshot />
    </div>
  );
}

export default Plants;
