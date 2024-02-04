import { cn } from "@/lib/utils";
import React from "react";

function Margins({ children, className }: any) {
  return (
    <div
      className={cn(
        "max-w-[1400px] 3xl:max-w-[1600px] w-[100%] h-[100%] mx-auto px-[30px]",
        className
      )}
    >
      {children}
    </div>
  );
}

export default Margins;
