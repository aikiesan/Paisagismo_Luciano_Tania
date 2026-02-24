# Deployment Guide — GitHub Pages

## ✅ Completed Steps

- [x] Directory structure created
- [x] 43 3D renders organized (scene-01 through scene-43)
- [x] Floor plan integrated
- [x] index.html created with responsive design
- [x] Configuration files (.gitignore, README.md)
- [x] Git repository initialized
- [x] Initial commit created

## 🚀 Next Steps: Deploy to GitHub Pages

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Fill in repository details:
   - **Repository name:** `projeto-luciano-tania` (or your preferred name)
   - **Description:** "Projeto de paisagismo residencial — Tanus Saab e Gustavo Valencio"
   - **Visibility:** Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (you already have these)
3. Click **Create repository**

### Step 2: Push to GitHub

After creating the repository, GitHub will show you commands. Use these in your terminal:

```bash
cd "A:\PROJETOS_PAISAGISMO\PROJETOS_2026\07_PROJETO_LUCIANO_GITHUBPAGES"

# Add the remote (replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/projeto-luciano-tania.git

# Push to GitHub
git push -u origin main
```

**Note:** Replace `USERNAME` with your actual GitHub username in the command above.

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (tab at the top)
3. Scroll down and click **Pages** (left sidebar)
4. Under "Source":
   - Branch: Select `main`
   - Folder: Select `/ (root)`
5. Click **Save**
6. GitHub will show: "Your site is ready to be published at `https://USERNAME.github.io/projeto-luciano-tania/`"

### Step 4: Wait for Deployment

- Deployment usually takes **1-3 minutes**
- Refresh the Settings → Pages section to see the green "Your site is live" message
- Visit your site at the URL provided

### Step 5: Verify Website

Check these elements on the live site:

- [ ] Logo displays correctly
- [ ] Hero section shows with background image
- [ ] Navigation works (desktop and mobile)
- [ ] All 43 renders load in the gallery
- [ ] Floor plan displays and opens in lightbox
- [ ] Lightbox opens when clicking images
- [ ] Mobile bottom navigation appears on small screens
- [ ] Scroll progress bar animates
- [ ] Species section shows placeholder message

## 📝 Optional: Update Plant Species

You already have 17 plant species images in the `especies_de_plantas/` folder:

1. Alocasia macrorrhiza (Orelha de Elefante)
2. Cortaderia selloana (Capim dos Pampas)
3. Eugenia uniflora (Pitanga)
4. Parthenocissus tricuspidata (Hera-falsa / Vinha-virgem)
5. Maranta (Maranta Charuto)
6. Malpighia emarginata (Acerola)
7. Morus nigra (Amora)
8. Syagrus romanzoffiana (Jerivá)
9. Thaumatophyllum bipinnatifidum (Filodendro)
10. Vachellia seyal (Acácia)
11. Zoysia japonica (Grama Esmeralda)
12. Filodendro ondulado
13. Ipê Amarelo
14. Jabuticabeira
15. Jasmim Manga
16. Congeia

To add these to the website:

1. **Move images to proper location:**
   ```bash
   mkdir -p public/images/species/thumbs
   cp especies_de_plantas/*.webp public/images/species/
   cp especies_de_plantas/*.webp public/images/species/thumbs/
   ```

2. **Edit index.html** (around line 891-905):
   - Replace the `.species-placeholder` section
   - Add species cards following the pattern in the README.md

3. **Commit and push:**
   ```bash
   git add public/images/species/ index.html
   git commit -m "Add plant species gallery"
   git push origin main
   ```

## 🔧 Troubleshooting

### Images not loading on GitHub Pages

If images don't appear after deployment:
- Verify all image paths are **relative** (no leading `/`)
- Check that image files are actually in the repository
- Clear browser cache and hard refresh (Ctrl+F5)

### 404 Error

If you get a 404 error:
- Check that GitHub Pages is enabled in Settings → Pages
- Verify the branch is set to `main` and folder to `/ (root)`
- Wait a few more minutes for deployment to complete

### Mobile navigation not working

- Test in different browsers
- Check browser console for JavaScript errors (F12)
- Verify the website works locally first

## 📞 Support

For issues or questions:
- Check the main README.md file
- Review the Casa EVA reference project
- Inspect browser console (F12) for errors

---

**Repository Location:** `A:\PROJETOS_PAISAGISMO\PROJETOS_2026\07_PROJETO_LUCIANO_GITHUBPAGES`

**Current Status:** ✅ Ready for GitHub deployment
