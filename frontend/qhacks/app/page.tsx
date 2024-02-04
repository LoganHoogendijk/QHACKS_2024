import Upload from "@/components/home/uploadImage";
import Margins from "@/components/margins";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { Outfit } from "next/font/google";
import Image from "next/image";
import Link from "next/link";
const roboto = Outfit({
  subsets: ["latin"],
});

export default function Home() {
  return (
    <main className="flex min-h-screen items-center justify-between ">
      <div className=" flex justify-center items-center absolute w-[35vw] z-0 top-0 right-0 h-[100vh] bg-themeSecondary">
        <Image
          src={"/qhackslogo.png"}
          height={400}
          width={238.36}
          alt="plant"
        />
      </div>
      <Margins className="z-10 ">
        <div className="flex flex-col items-start gap-[30px]">
          <div>
            <h1
              className={cn(
                "text-title font-[700] tracking-widest leading-tight",
                roboto.className
              )}
            >
              LeafHack
            </h1>
            <h2 className="text-smSubheading font-[300] text-[#6c6c6c]">
              Track your plant's health with the snap of a photo.
            </h2>
          </div>
          <Link href={"/login"}>
            <Button>Get Started</Button>
          </Link>
        </div>
      </Margins>
      {/* <Upload /> */}
    </main>
  );
}
