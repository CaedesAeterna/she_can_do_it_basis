# Project Status Document
**Date:** 2026-01-19
**Project Name:** she-can-do-it-basis

## Overview
This project is a **NestJS Monorepo** containing two distinct applications designed for a food waste management system.

### Applications

#### 1. Food Waste Customer (`apps/food-waste-customer`)
- **Purpose:** Client-facing application for users.
- **Port:** 3000
- **Key Modules:**
  - `UserModule`: Handles authentication (`AuthController`) and user profiles (`ProfileController`).
- **Entry Point:** `apps/food-waste-customer/src/main.ts`

#### 2. Food Waste CMS (`apps/food-waste-cms`)
- **Purpose:** Admin and management dashboard.
- **Port:** 3001
- **Key Modules:**
  - `RestaurantModule`: Manages restaurant data.
  - `CustomersModule`: Manages customer data from an admin perspective.
- **Entry Point:** `apps/food-waste-cms/src/main.ts`

## Development Commands

### Running Applications
- **Customer App:** `npm run start:food-waste-customer`
- **CMS App:** `npm run start:food-waste-cms`
- **Development Mode (Watch):**
  - Use `nest start --watch food-waste-customer` or `nest start --watch food-waste-cms`

### Building
- **Build All:** `npm run build`
- **Build Specific:** `nest build food-waste-customer` or `nest build food-waste-cms`

### Testing
- **Unit Tests:** `npm run test`
- **E2E Tests:** `npm run test:e2e`
- **Coverage:** `npm run test:cov`

## Project Structure
```
/
├── apps/
│   ├── food-waste-cms/       # Admin Application
│   └── food-waste-customer/  # User Application
├── dist/                     # Compiled output
├── libs/                     # Shared libraries (currently empty)
├── nest-cli.json             # Monorepo configuration
├── package.json              # Dependencies and scripts
└── tsconfig.json             # TypeScript configuration
```

## Dependencies
- **Core:** `@nestjs/common`, `@nestjs/core`, `@nestjs/platform-express`
- **Testing:** `jest`, `supertest`
- **Linting:** `eslint`, `prettier`
