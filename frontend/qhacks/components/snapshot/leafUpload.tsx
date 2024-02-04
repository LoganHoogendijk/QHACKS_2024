import React, { useState } from "react";
import {
  Dialog,
  DialogFooter,
  DialogHeader,
  DialogTrigger,
  DialogDescription,
  DialogContent,
  DialogTitle,
} from "../ui/dialog";
import { Input } from "../ui/input";
import { Label } from "../ui/label";
import { postCrop } from "@/lib/utils";
import { Button } from "../ui/button";
import Image from "next/image";
import { useData } from "@/context/dataContext";
import { useAuth } from "@/context/authContext";
import { DialogClose } from "@radix-ui/react-dialog";
import { useRouter } from "next/navigation";

function LeafUpload({ children }: any) {
  const [leafImage, setLeafImage] = useState<any>(null);
  const [cropLabel, setCropLabel] = useState("");

  const { setPlants, setSelectedPlant} = useData();
  const { csrf, user } = useAuth();
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const handleUpload = (event: any) => {
    setLeafImage(event.target.files[0]);
  };

  const submitForm = async (e: any) => {
    e.preventDefault();
    const res = await postCrop(leafImage, cropLabel, csrf, user.user);

    setSelectedPlant(res);

    router.push("/plant?plantId=0")
  };

  const deleteLeafImage = () => {
    setLeafImage(null);
  };

  return (
    <Dialog>
      <DialogTrigger asChild>{children}</DialogTrigger>

      <DialogContent>
        <DialogHeader>
          <DialogTitle className="!text-subheading text-themeBtns leading-normal">
            Leaf Photo Upload
          </DialogTitle>
          <DialogDescription>
            Submit a photo of the leave of your plant to analyze its health.
          </DialogDescription>
        </DialogHeader>
        <Label htmlFor="name">Plant Name:</Label>
        <Input
          id="name"
          type="text"
          value={cropLabel}
          onChange={(e) => {
            setCropLabel(e.target.value);
          }}
        />
        <Label htmlFor="leaf">Select Leaf Image:</Label>
        {leafImage ? (
          <div className="flex items-center gap-[10px]">
            <Label className="text-themeMidGreen">{leafImage?.name}</Label>
            <button onClick={() => deleteLeafImage()}>
              <Image src={"/delete.svg"} height={10} width={10} alt="delete" />
            </button>
          </div>
        ) : (
          <Label
            htmlFor="leaf"
            className="gap-[10px] cursor-pointer border-[2px] border-themeBtns text-themeBtns hover:bg-themePrimary inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 h-10 px-4 py-2"
          >
            Upload Photo
            <Image src="/camera.svg" alt="camera" height={25} width={25} />
          </Label>
        )}
        <Input
          id="leaf"
          type="file"
          capture="environment"
          accept="image/*"
          onChange={handleUpload}
          className="text-black"
          style={{ display: "none" }}
        />

        <DialogFooter className="mt-[20px]">
          {loading ? (
            <div className="flex">
              <div className="h-[5px] w-[5px] bg-themeBtns rounded-[50%]"></div>
              <div className="h-[5px] w-[5px] bg-themeBtns rounded-[50%]"></div>
              <div className="h-[5px] w-[5px] bg-themeBtns rounded-[50%]"></div>
            </div>
          ) : (
            <Button onClick={(e) => submitForm(e)}>Analyze Leaf</Button>
          )}
        </DialogFooter>
        <DialogClose id="close"></DialogClose>
      </DialogContent>
    </Dialog>
  );
}

export default LeafUpload;
