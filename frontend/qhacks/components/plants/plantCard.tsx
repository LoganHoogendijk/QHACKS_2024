"use client";
import React from "react";
import { Card } from "../ui/card";
import { Badge } from "../ui/badge";
import Image from "next/image";
import Link from "next/link";

function PlantCard({ plant, id }: any) {
  console.log(plant);
  return (
    <Link href={`/plant?plantId=${id}`}>
      <Card className="min-h-[300px] shadow-md flex justify-between overflow-hidden hover:scale-[1.005] transition-all cursor-pointer">
        <div className="flex flex-col w-[100%]">
          <div className="bg-themeSecondary relative w-[100%] min-h-[200px] flex justify-center items-center">
            <Image
              src="/qhackslogo.png"
              className=" p-5 object-contain"
              alt="your leaf"
              fill
            />
          </div>
          <div className="p-5 flex flex-col gap-[10px] items-start">
            <h1 className="text-subheading">Plant # {plant}</h1>
            <Badge className="bg-themeBtns border-[2px] border-themeBtns text-white font-normal">
              Healthy
            </Badge>
          </div>
        </div>
      </Card>
    </Link>
  );
}

export default PlantCard;
