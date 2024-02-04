"use client";
import Image from "next/image";
import React from "react";
import Margins from "../margins";
import Link from "next/link";
import { cn } from "@/lib/utils";
import { Outfit } from "next/font/google";
import { Button } from "../ui/button";
const outfit = Outfit({
  subsets: ["latin"],
});
function Nav() {
  return (
    <nav className="z-[12] fixed top-0 left-0 right-0">
      <Margins className="py-[15px] flex justify-between">
        <Link href="/">
          <div className="flex gap-[20px] items-end">
            <Image src="/qhackslogo.png" alt="plant" width={23} height={40} />
            <h1
              className={cn(
                "text-body font-[700] tracking-widest leading-tight",
                outfit.className
              )}
            >
              LeafHack
            </h1>
          </div>
        </Link>
        <div className="flex gap-[40px] items-center">
          {/* <Link href="/plants"></Link> */}
          <Link
            href="/plants"
            className="text-themeBtns font-[500] hover:text-themeBtns/65 hover:border-themeBtns/65 border-b-[2px] border-transparent transition-all"
          >
            Garden
          </Link>
          <Link href="/login">
            <Button className="bg-themeBtns font-[500]">Login</Button>
          </Link>
        </div>
      </Margins>
    </nav>
  );
}

export default Nav;
