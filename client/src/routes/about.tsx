import { Github, Smile } from 'lucide-react'

function About() {
  return (
    <div className="flex flex-row justify-center">
      <div className="flex flex-col justify-start p-16">
        <div className="rounded-2xl bg-purple_medium p-16">
          <h1 className="text-center font-chapeau text-5xl font-light text-black">
            About this app
          </h1>
          <p className="mt-8 text-center">
            This is a simple React application that uses TypeScript, ESLint, and
            Prettier.
          </p>
          <div className="mt-8 flex flex-row justify-center gap-2">
            <p>Code is available on</p>
            <a
              className="flex flex-row gap-2"
              href="https://github.com/AdrianDevs/RnD"
              target="_blank"
              rel="noopener noreferrer"
            >
              <Github color="black" />
              <span className="text-green_dark underline hover:text-purple_dark">
                GitHub
              </span>
            </a>
          </div>
        </div>
        <div className="mt-8 rounded-2xl bg-green_medium p-16">
          <h1 className="text-center font-chapeau text-5xl font-light text-black">
            About me
          </h1>
          <div className="mt-8 flex flex-row items-center justify-center gap-2">
            <p className="text-center text-xl">Just ask</p>{' '}
            <Smile color="black" />
          </div>
        </div>
      </div>
    </div>
  )
}

export default About
