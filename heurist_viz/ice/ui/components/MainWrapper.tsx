import React from "react";
import "/styles/globals.css";
import "/styles/dark-theme.css";
import { css, Global } from "@emotion/react";
import { ChakraWrapper } from "/components/ChakraWrapper/ChakraWrapper";
import { Box, HStack, Image } from "@chakra-ui/react";

const GlobalStyles = css`
  // Remove Chakra focus outline is the element is not actually focussed
  // See https://github.com/chakra-ui/chakra-ui/issues/708
  [data-focus]:not(:focus) {
    box-shadow: none !important;
  }
  // TODO (jason) Fixed in https://github.com/chakra-ui/chakra-ui/pull/5969,
  // but we can't upgrade till we remove Mui
  .chakra-popover__popper {
    min-width: unset !important;
  }

  * {
    box-sizing: border-box;
  }

  html,
  body,
  #__next {
    margin: 0;
    padding: 0;
    height: 100%;
  }

  h1,
  h2,
  h3 {
    margin: 0;
    padding: 0;
  }

  body {
    font-family: Roboto, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu,
      Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif;
    line-height: 1.5;
  }

  a {
    text-decoration: none;
  }

  a,
  a:visited {
    color: #3d90fb;
  }

  a:hover {
    cursor: pointer;
  }

  main {
    flex-grow: 1;
    display: flex;
    flex-flow: column;
  }
`;

export const MainWrapper = ({ children }: { children: React.ReactNode }) => (
  <React.StrictMode>
    <ChakraWrapper>
      <Global styles={GlobalStyles} />
      <Box as="header" borderBottom="1px solid" borderColor="gray.700" p={4} bg="#1a1a1a">
        <HStack spacing={4} align="center">
          <Image 
            src="/assets/heurist-logo-white.svg" 
            alt="Heurist Logo"
            height="50px"
            width="auto"
          />
          <Box 
            as="h1" 
            fontSize="3xl" 
            fontWeight="medium" 
            color="white"
          >
            Heurist Trace Visualizer
          </Box>
        </HStack>
      </Box>
      {children}
    </ChakraWrapper>
  </React.StrictMode>
);
