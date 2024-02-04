"use client";
import Margins from "@/components/margins";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
  type CarouselApi,
} from "@/components/ui/carousel";
import { Checkbox } from "@/components/ui/checkbox";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useAuth } from "@/context/authContext";
import { useData } from "@/context/dataContext";
import { getImage } from "@/lib/utils";
import Image from "next/image";
import { useSearchParams } from "next/navigation";
import React, { useEffect, useState } from "react";
function Plant() {
  const params = useSearchParams();
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(true);
  const { selectedPlant } = useData();
  const { csrf, user } = useAuth();

  useEffect(() => {
    const fetchImage = async () => {
      const res = await getImage(selectedPlant.crop, csrf);
      const imageUrl = res[0].image;
      setUrl(imageUrl);
      setLoading(false);
    };
    fetchImage();
  }, []);

  return (
    <div className="flex justify-center items-center min-h-[100vh] w-[100%]">
      <Margins className="flex flex-col justify-center gap-[50px] py-[100px]">
        {!loading && (
          <>
            {/* Content */}
            <div className="grid grid-cols-2 h-[100%] w-[100%] gap-[30px] min-h-[500px] max-h-[900px]">
              {/* Image */}
              <div className="rounded-[15px] overflow-hidden relative max-h-[800px] h-[100%] shadow-lg flex justify-start min-w-[400px] max-w-[750px]">
                <Image src={url} alt="plant" fill className="object-cover " />
              </div>

              {/* Plant Content */}
              <div className="flex items-start justify-start flex-col gap-[30px]  p-[30px] h-[100%] rounded-lg">
                <div className=" flex flex-col gap-[5px]">
                  <div className=" font-[500] !text-themeBtns text-title">
                    {selectedPlant?.output["Plant Type"]}
                  </div>
                  <div className="flex flex-col gap-[10px] items-start">
                    <div className="!text-body text-mutedText">2024-02-04</div>
                    <Badge className="bg-themePrimary border-[2px] border-themeBtns text-black font-normal">
                      {selectedPlant?.output?.Disease}
                    </Badge>
                    <Badge className="bg-themePrimary border-[2px] border-themeBtns text-black font-normal">
                      {selectedPlant?.output?.Healthy == 1
                        ? "Healthy"
                        : "Unhealthy"}
                    </Badge>
                  </div>
                </div>
                <div className="flex flex-col justify-star h-[100%]">
                  <h2 className="text-subheading font-[400]  text-themeBtns/85 mb-[15px]">
                    Recommendations
                  </h2>
                  <ul className="flex flex-col justify-start items-start gap-[17px] w-[100%]">
                    {selectedPlant?.output?.recommendations.map(
                      (recommendation: any, key: any) => (
                        <div
                          key={key}
                          className="flex justify-start w-[100%] items-center gap-[10px]"
                        >
                          <Checkbox id={"recommendation" + key} />
                          <Label
                            className="!text-body font-normal cursor-pointer tracking-wide"
                            htmlFor={"recommendation" + key}
                          >
                            {recommendation}
                          </Label>
                        </div>
                      )
                    )}
                  </ul>
                </div>
              </div>
            </div>
          </>
        )}
      </Margins>
    </div>
  );
}

export default Plant;
