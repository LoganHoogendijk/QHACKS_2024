"use client";
import React, { useEffect } from "react";
import Plant from "./plantCard";
import { useAuth } from "@/context/authContext";
import { useData } from "@/context/dataContext";
import { userProfile } from "@/lib/utils";
import Plants from "@/app/plants/page";

function PlantsList() {
  const { user } = useAuth();
  const { plants, setPlants } = useData();

  useEffect(() => {
    if (user) {
      // console.log(user);
      // setPlants(user.crops);
    }
  }, [user]);
  return (
    <div className="grid grid-cols-4 justify-center gap-[20px] w-[100%] ">
      {plants.length > 0 ? (
        plants.map((plant, id) => <Plant plant={plant} />)
      ) : (
        <div className="flex justify-center items-center w-[100%] col-span-4 ">
          No Crops available...
        </div>
      )}
    </div>
  );
}

export default PlantsList;
