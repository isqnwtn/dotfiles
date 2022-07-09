;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!


;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets. It is optional.
(setq user-full-name "Vismay Raj"
      user-mail-address "vismayraj1@gmail.com")

;; Doom exposes five (optional) variables for controlling fonts in Doom:
;;
;; - `doom-font' -- the primary font to use
;; - `doom-variable-pitch-font' -- a non-monospace font (where applicable)
;; - `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;; - `doom-unicode-font' -- for unicode glyphs
;; - `doom-serif-font' -- for the `fixed-pitch-serif' face
;;
;; See 'C-h v doom-font' for documentation and more examples of what they
;; accept. For example:
;;
;;(setq doom-font (font-spec :family "Fira Code" :size 12 :weight 'semi-light)
;;      doom-variable-pitch-font (font-spec :family "Fira Sans" :size 13))
;;
;; If you or Emacs can't find your font, use 'M-x describe-font' to look them
;; up, `M-x eval-region' to execute elisp code, and 'M-x doom/reload-font' to
;; refresh your font settings. If Emacs still can't find your font, it likely
;; wasn't installed correctly. Font issues are rarely Doom issues!

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-1337
      doom-font (font-spec :family "FiraMono NF" :size 15 :weight 'light)
      doom-variable-pitch-font (font-spec :family "FiraMono NF" :size 15))
;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type t)

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/org/")


;; Whenever you reconfigure a package, make sure to wrap your config in an
;; `after!' block, otherwise Doom's defaults may override your settings. E.g.
;;
;;   (after! PACKAGE
;;     (setq x y))
;;
;; The exceptions to this rule:
;;
;;   - Setting file/directory variables (like `org-directory')
;;   - Setting variables which explicitly tell you to set them before their
;;     package is loaded (see 'C-h v VARIABLE' to look up their documentation).
;;   - Setting doom variables (which start with 'doom-' or '+').
;;
;; Here are some additional functions/macros that will help you configure Doom.
;;
;; - `load!' for loading external *.el files relative to this one
;; - `use-package!' for configuring packages
;; - `after!' for running code after a package has loaded
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;; Alternatively, use `C-h o' to look up a symbol (functions, variables, faces,
;; etc).
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.

;; Custom
;;
;; My Functions
(load! "myfunctions.el")

;; opens emacs in full screen
(add-to-list 'default-frame-alist '(fullscreen . maximized))

;; disable exit confirmation
;; (setq confirm-kill-emacs nil)

(map! :leader
      :desc "Vertical Vterm here"
      "o i" #'my-vterm/split-right)


;; pop up rules
(set-popup-rule! "^\\*help" :side 'right :size 0.6)
(set-popup-rule! "^\\*doom:vterm-popup" :side 'right :size '+popup-shrink-to-fit :ttl nil)

;; this sets the shell variable inside emacs
(cl-loop for file in '("/usr/bin/zsh")
        when (file-exists-p file)
        do (progn
        (setq shell-file-name file)
        (cl-return)))
(setenv "SHELL" shell-file-name)

;; setting emacs exec path from shell path
;; the function is defined in myfunctions.el
;; (set-exec-path-from-shell-PATH)
;; in case the other thing doesnt work
;; this is usefull for running haskell-language-server (pretty much solved the issue I had with it)
;; (setenv "PATH" (concat (getenv "PATH") ":/home/vismay/.cabal/bin")
;; (setq exec-path (append exec-path '("/home/vismay/.cabal/bin")))

(setenv "PATH" (concat (getenv "PATH") ":/home/vismay/.ghcup/bin"))
(setq exec-path (append exec-path '("/home/vismay/.ghcup/bin")))

(setenv "PATH" (concat (getenv "PATH") ":/home/vismay/.cabal/bin"))
(setq exec-path (append exec-path '("/home/vismay/.cabal/bin")))


;; haskell lsp?? I've no clue where to add these so im adding it here lmao
(add-hook 'haskell-mode-hook #'lsp)
(add-hook 'haskell-literate-mode-hook #'lsp)

(after!
  (setq lsp-haskell-formatting-provider "brittany"))

;; stylish haskell
(setq haskell-stylish-on-save t)

;; transparent apparently!!!
(set-frame-parameter (selected-frame)'alpha '(90 . 90))
(add-to-list 'default-frame-alist'(alpha . (90 . 90)))
;;(set-frame-parameter (selected-frame) 'alpha 85)
;;(add-to-list 'default-frame-alist '(alpha . 85))


;; Latex  Org
(add-hook 'org-mode-hook 'org-fragtog-mode)
(setq org-latex-packages-alist '())
(add-to-list 'org-latex-packages-alist
             '("" "tikz" t))

(eval-after-load "preview"
  '(add-to-list 'preview-default-preamble "\\PreviewEnvironment{tikzpicture}" t))

(setq org-latex-create-formula-image-program 'dvisvgm)
(after!
  (setq org-format-latex-options (plist-put org-format-latex-options :scale 1.1))
  )
;;(after! org (plist-put org-format-latex-options :scale 1.1)
;; Spelling and stuff
(setq-default ispell-program-name "aspell")
