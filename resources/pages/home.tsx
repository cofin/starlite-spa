import { Head } from "@inertiajs/react"
import { AppLayout } from "@/layouts/app-layout"
import { Header } from "@/components/header"
import { Container } from "@/components/container"
import { Icons } from "@/components/icons"

import { BeakerIcon } from "lucide-react"
export default function Home() {
  return (
    <>
      <Head title="Welcome to Litestar" />
      <Header title="Inertia Typescript" />
      <Container>
        <div className="overflow-hidden rounded-lg border">
          <div>
            <div className="p-4 sm:p-20">
              <div>
                <svg
                  viewBox="0 52 410 250"
                  xmlns="http://www.w3.org/2000/svg"
                  className="block h-12 w-auto fill-current text-red-500"
                >
                  <defs>
                    <clipPath id="9eb7762d41">
                      <path
                        d="M 15.933594 105 L 328 105 L 328 259 L 15.933594 259 Z M 15.933594 105 "
                        clipRule="nonzero"
                      />
                    </clipPath>
                    <clipPath id="183d3cc178">
                      <path
                        d="M 142 78.769531 L 359.433594 78.769531 L 359.433594 296.269531 L 142 296.269531 Z M 142 78.769531 "
                        clipRule="nonzero"
                      />
                    </clipPath>
                  </defs>
                  <g clipPath="url(#9eb7762d41)">
                    <path
                      fill="#edb641"
                      d="M 147.625 240.3125 C 161.5 233.984375 173.554688 227.011719 183.425781 220.550781 C 202.304688 208.203125 226.4375 185.242188 227.761719 183.410156 L 218.917969 177.503906 L 211.257812 172.386719 L 235.503906 171.441406 L 243.296875 171.136719 L 245.414062 163.640625 L 252.007812 140.304688 L 260.402344 163.054688 L 263.097656 170.363281 L 270.890625 170.058594 L 295.136719 169.113281 L 276.078125 184.117188 L 269.953125 188.9375 L 272.652344 196.25 L 281.046875 218.996094 L 260.871094 205.523438 L 254.390625 201.195312 L 248.265625 206.015625 L 229.207031 221.023438 L 232.480469 209.425781 L 235.796875 197.691406 L 236.207031 196.234375 C 213.003906 213.585938 180.546875 230.304688 161.140625 236.488281 C 156.6875 237.90625 152.183594 239.179688 147.625 240.3125 Z M 101.992188 258.078125 C 136.382812 256.734375 177.355469 248 217.675781 222.363281 L 209.90625 249.867188 L 254.910156 214.4375 L 302.539062 246.246094 L 282.71875 192.539062 L 327.71875 157.109375 L 270.46875 159.34375 L 250.648438 105.636719 L 235.085938 160.726562 L 177.835938 162.964844 L 210.980469 185.097656 C 189.164062 204.921875 134.445312 247.195312 61.957031 250.03125 C 47.300781 250.601562 31.914062 249.558594 15.933594 246.394531 C 15.933594 246.394531 52.011719 260.035156 101.992188 258.078125 "
                      fillOpacity="1"
                      fillRule="nonzero"
                    />
                  </g>
                  <g clipPath="url(#183d3cc178)">
                    <path
                      fill="#edb641"
                      d="M 250.789062 78.96875 C 190.78125 78.96875 142.140625 127.570312 142.140625 187.519531 C 142.140625 198.875 143.886719 209.816406 147.121094 220.101562 C 151.847656 217.75 156.363281 215.316406 160.660156 212.84375 C 158.394531 204.789062 157.183594 196.296875 157.183594 187.519531 C 157.183594 135.871094 199.089844 93.996094 250.789062 93.996094 C 302.484375 93.996094 344.390625 135.871094 344.390625 187.519531 C 344.390625 239.171875 302.484375 281.042969 250.789062 281.042969 C 222.75 281.042969 197.597656 268.722656 180.441406 249.210938 C 175.453125 251.152344 170.402344 252.917969 165.289062 254.511719 C 185.183594 279.816406 216.082031 296.070312 250.789062 296.070312 C 310.792969 296.070312 359.433594 247.472656 359.433594 187.519531 C 359.433594 127.570312 310.792969 78.96875 250.789062 78.96875 "
                      fillOpacity="1"
                      fillRule="nonzero"
                    />
                  </g>
                  <path
                    fill="#edb641"
                    d="M 92.292969 173.023438 L 98.289062 191.460938 L 117.691406 191.460938 L 101.992188 202.855469 L 107.988281 221.292969 L 92.292969 209.898438 L 76.59375 221.292969 L 82.589844 202.855469 L 66.894531 191.460938 L 86.296875 191.460938 L 92.292969 173.023438 "
                    fillOpacity="1"
                    fillRule="nonzero"
                  />
                  <path
                    fill="#edb641"
                    d="M 120.214844 112.25 L 125.390625 128.167969 L 142.140625 128.167969 L 128.589844 138 L 133.765625 153.917969 L 120.214844 144.082031 L 106.664062 153.917969 L 111.839844 138 L 98.289062 128.167969 L 115.039062 128.167969 L 120.214844 112.25 "
                    fillOpacity="1"
                    fillRule="nonzero"
                  />
                  <path
                    fill="#edb641"
                    d="M 34.695312 209.136719 L 37.71875 218.421875 L 47.492188 218.421875 L 39.585938 224.160156 L 42.605469 233.449219 L 34.695312 227.707031 L 26.792969 233.449219 L 29.8125 224.160156 L 21.90625 218.421875 L 31.679688 218.421875 L 34.695312 209.136719 "
                    fillOpacity="1"
                    fillRule="nonzero"
                  />
                </svg>
              </div>
              <div className="max-w-2xl">
                <div className="mt-6 text-xl sm:mt-8 sm:text-2xl">
                  Litestar application with Inertia and React Typescript!
                </div>
                <div className="mt-4 text-muted-foreground sm:mt-6 sm:text-lg">
                  This is a Litestar application with Inertia and React
                  Typescript. It is a work in progress. If you have any
                  questions or suggestions, please feel free to contact me.
                </div>
              </div>

              <div className="mt-16 grid gap-4 lg:grid-cols-2">
                <div className="rounded-xl border bg-secondary/20 p-8">
                  <a
                    href="https://github.com/litestar-org/litestar-fullstack"
                    className="flex items-center gap-x-2 font-semibold text-primary"
                    target="_blank"
                  >
                    <Icons.gitHub className="size-8 stroke-1" />
                    Litestar
                  </a>
                  <p className="mt-5 text-muted-foreground">
                    This project is developed by{" "}
                    <a
                      href="https://litestar.dev"
                      target="_blank"
                      className="text-foreground font-semibold"
                    >
                      Litestar
                    </a>
                    , if you want to contribute to this project, please visit
                    the{" "}
                    <a
                      href="https://github.com/litestar-org/litestar-fullstack"
                      target="_blank"
                      className="text-foreground font-semibold"
                    >
                      Github Repository
                    </a>
                    .
                  </p>
                </div>
                <div className="rounded-xl border bg-secondary/20 p-8">
                  <a
                    href="https://github.com/litestar-org/litestar-fullstack"
                    className="flex items-center gap-x-2 font-semibold text-primary"
                    target="_blank"
                  >
                    <Icons.inertia className="size-8 stroke-1" />
                    Inertia
                  </a>
                  <p className="mt-5 text-muted-foreground">
                    Create modern single-page React, Vue, and Svelte apps using
                    classic server-side routing. Works with any backend.
                  </p>
                </div>

                <div className="rounded-xl border bg-secondary/20 p-8">
                  <a
                    href="https://paranoid.irsyad.co"
                    className="flex items-center gap-x-2 font-semibold text-primary"
                    target="_blank"
                  >
                    <BeakerIcon className="size-8" />
                    Advanced Alchemy
                  </a>
                  <p className="mt-5 text-muted-foreground">
                    A carefully crafted, thoroughly tested, optimized companion
                    library for SQLAlchemy
                  </p>
                </div>
                <div className="rounded-xl border bg-secondary/20 p-8">
                  <a
                    href="https://irsyad.co/s"
                    className="flex items-center gap-x-2 font-semibold text-primary"
                    target="_blank"
                  >
                    <Icons.react className="size-8" />
                    React Template
                  </a>
                  <p className="mt-5 text-muted-foreground">
                    Explore the next.js templates from web apps to design
                    systems, all here.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Container>
    </>
  )
}

Home.layout = (page: any) => <AppLayout children={page} />
