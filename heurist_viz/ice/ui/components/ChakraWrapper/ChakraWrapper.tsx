import { ChakraProvider, extendTheme } from "@chakra-ui/react";
import createCache from "@emotion/cache";
import { CacheProvider } from "@emotion/react";
import { ReactNode } from "react";
import { alertStyles } from "./alertStyles";
import { buttonStyles } from "./buttonStyles";
import { inputStyles } from "./inputStyles";
import { tabStyles } from "./tabsStyles";
import { tagStyles } from "./tagStyles";
import { textareaStyles } from "./textareaStyles";
import * as COLORS from "/styles/colors.json";

const emotionCache = createCache({
  key: "emotion-css-cache",
  prepend: true,
});

export interface ThemingInfo {
  colorMode: string; // eg light, dark
  colorScheme: string; // eg blue
  size: "xs" | "sm" | "md" | "lg";
}

const theme = extendTheme({
  config: {
    initialColorMode: 'dark',
    useSystemColorMode: false,
  },
  styles: {
    global: {
      body: {
        bg: 'gray.800',
        color: 'white'
      }
    }
  },
  components: {
    Input: inputStyles,
    Textarea: textareaStyles,
    Button: buttonStyles,
    Tag: tagStyles,
    Alert: alertStyles,
    Tabs: tabStyles,
    Box: {
      baseStyle: {
        bg: 'gray.800',
        color: 'white',
      }
    },
    Menu: {
      baseStyle: {
        list: {
          bg: 'gray.800',
          borderColor: 'gray.600',
        },
        item: {
          bg: 'gray.800',
          _hover: {
            bg: 'gray.700',
          },
        },
      }
    },
    HStack: {
      baseStyle: {
        bg: 'gray.800',
      }
    },
    FormControl: {
      baseStyle: {
        color: 'white',
      }
    },
    Switch: {
      baseStyle: {
        track: {
          bg: 'gray.600',
          _checked: {
            bg: 'blue.500',
          }
        }
      }
    }
  },
  colors: COLORS,
});

// TODO (jason) put the css reset in here
export const ChakraWrapper = ({ children }: { children: ReactNode }) => (
  <CacheProvider value={emotionCache}>
    <ChakraProvider resetCSS theme={theme}>
      {children}
    </ChakraProvider>
  </CacheProvider>
);
